import React, { useEffect, useState } from 'react'
import ReactDOM from 'react-dom/client'
import './style.css'

const API_URL = 'http://127.0.0.1:8000'

type User = {
  id: number
  name: string
  created_at: string
}

type Conversation = {
  id: number
  title: string
  created_at: string
  participants: Array<{ id: number; name: string }>
}

type Message = {
  id: number
  content: string
  created_at: string
  conversation_id: number
  sender: { id: number; name: string }
}

type Theme = 'system' | 'light' | 'dark'

async function request<T>(path: string, options?: RequestInit): Promise<T> {
  const response = await fetch(`${API_URL}${path}`, {
    headers: { 'Content-Type': 'application/json' },
    ...options,
  })

  if (!response.ok) {
    const payload = (await response.json().catch(() => null)) as { detail?: string } | null
    throw new Error(payload?.detail ?? 'Something went wrong.')
  }

  if (response.status === 204) {
    return undefined as T
  }

  return (await response.json()) as T
}

function App() {
  const [users, setUsers] = useState<User[]>([])
  const [conversations, setConversations] = useState<Conversation[]>([])
  const [messages, setMessages] = useState<Message[]>([])
  const [activeConversationId, setActiveConversationId] = useState<number | null>(null)
  const [newUserName, setNewUserName] = useState('')
  const [newConversationTitle, setNewConversationTitle] = useState('')
  const [selectedParticipants, setSelectedParticipants] = useState<number[]>([])
  const [senderId, setSenderId] = useState<number | ''>('')
  const [newMessage, setNewMessage] = useState('')
const [error, setError] = useState('')
const [loadingMessages, setLoadingMessages] = useState(false)
  const [theme, setTheme] = useState<'system' | 'light' | 'dark'>('system')
  const [menuId, setMenuId] = useState<number | null>(null)
  const [replyTo, setReplyTo] = useState<{id: number, name: string, content: string} | null>(null)

  const html = document.documentElement

  async function loadUsers() {
    setUsers(await request<User[]>('/users'))
  }

  async function loadConversations() {
    const nextConversations = await request<Conversation[]>('/conversations')
    setConversations(nextConversations)
    if (nextConversations.length === 0) {
      setActiveConversationId(null)
      setMessages([])
      return
    }
    setActiveConversationId((current) =>
      current && nextConversations.some((item) => item.id === current)
        ? current
        : nextConversations[0].id,
    )
  }

  async function loadMessages(conversationId: number) {
    setLoadingMessages(true)
    try {
      setMessages(await request<Message[]>(`/conversations/${conversationId}/messages`))
    } finally {
      setLoadingMessages(false)
    }
  }

  useEffect(() => {
    void Promise.all([loadUsers(), loadConversations()]).catch((err: Error) =>
      setError(err.message),
    )
  }, [])

  useEffect(() => {
    if (activeConversationId === null) {
      return
    }
    void loadMessages(activeConversationId).catch((err: Error) => setError(err.message))
  }, [activeConversationId])

  // Theme persistence
  useEffect(() => {
    const saved = localStorage.getItem('theme') as Theme | null
    if (saved) setTheme(saved)
  }, [])

  useEffect(() => {
    localStorage.setItem('theme', theme)
    const isDark = theme === 'dark' || (theme === 'system' && window.matchMedia('(prefers-color-scheme: dark)').matches)
    html.classList.toggle('dark', isDark)
  }, [theme])

  useEffect(() => {
    const mediaQuery = window.matchMedia('(prefers-color-scheme: dark)')
    const handleChange = () => {
      if (theme === 'system') {
        const isDark = mediaQuery.matches
        html.classList.toggle('dark', isDark)
      }
    }
    mediaQuery.addEventListener('change', handleChange)
    return () => mediaQuery.removeEventListener('change', handleChange)
  }, [theme])

  async function handleCreateUser(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault()
    setError('')
    try {
      await request<User>('/users', {
        method: 'POST',
        body: JSON.stringify({ name: newUserName }),
      })
      setNewUserName('')
      await loadUsers()
    } catch (err) {
      setError((err as Error).message)
    }
  }

  async function handleDeleteUser(userId: number) {
    setError('')
    try {
      await request<void>(`/users/${userId}`, { method: 'DELETE' })
      await Promise.all([loadUsers(), loadConversations()])
    } catch (err) {
      setError((err as Error).message)
    }
  }

  async function handleCreateConversation(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault()
    setError('')
    try {
      const created = await request<Conversation>('/conversations', {
        method: 'POST',
        body: JSON.stringify({
          title: newConversationTitle,
          participant_ids: selectedParticipants,
        }),
      })
      setNewConversationTitle('')
      setSelectedParticipants([])
      await loadConversations()
      setActiveConversationId(created.id)
    } catch (err) {
      setError((err as Error).message)
    }
  }

  async function handleDeleteConversation(conversationId: number) {
    setError('')
    try {
      await request<void>(`/conversations/${conversationId}`, { method: 'DELETE' })
      await loadConversations()
    } catch (err) {
      setError((err as Error).message)
    }
  }

  async function handleSendMessage(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault()
    if (activeConversationId === null) {
      return
    }
    setError('')
    try {
      await request<Message>(`/conversations/${activeConversationId}/messages`, {
        method: 'POST',
        body: JSON.stringify({ sender_id: senderId, content: newMessage }),
      })
      setNewMessage('')
      setReplyTo(null)
      await loadMessages(activeConversationId)
    } catch (err) {
      setError((err as Error).message)
    }
  }

  async function copyToClipboard(text: string) {
    try {
      await navigator.clipboard.writeText(text)
      // Optional: show toast
      setError('Copied to clipboard!')
      setTimeout(() => setError(''), 2000)
    } catch (err) {
      setError('Copy failed')
    }
  }

  async function handleDeleteMessage(messageId: number) {
    setError('')
    try {
      await request<void>(`/messages/${messageId}`, { method: 'DELETE' })
      if (activeConversationId !== null) {
        await loadMessages(activeConversationId)
      }
    } catch (err) {
      setError((err as Error).message)
    }
  }

  function cycleTheme() {
    const themes: Theme[] = ['system', 'light', 'dark']
    const currentIndex = themes.indexOf(theme)
    const nextTheme = themes[(currentIndex + 1) % themes.length]
    setTheme(nextTheme)
  }

  const activeConversation =
    conversations.find((conversation) => conversation.id === activeConversationId) ?? null

  return (
    <div className="app-shell">
<header className="hero">
        <div className="hero-content">
          <p className="eyebrow">Simple starter</p>
          <h1>Chat CRUD with React + FastAPI</h1>
          <p className="hero-copy">
            Create users, open a chat, and send messages. The backend uses SQLite for
            now, but the API shape stays simple enough to swap the storage layer later.
          </p>
        </div>
        <button 
          onClick={cycleTheme}
          className="theme-toggle"
          title="Toggle theme"
        >
          {theme === 'light' ? '🌙' : theme === 'dark' ? '☀️' : '🔄'}
        </button>
      </header>

      {error ? <div className="error-banner">{error}</div> : null}

      <main className="layout">
        <section className="panel">
          <div className="panel-heading">
            <h2>Users</h2>
            <span>{users.length}</span>
          </div>
          <form className="stack" onSubmit={handleCreateUser}>
            <input
              value={newUserName}
              onChange={(event) => setNewUserName(event.target.value)}
              placeholder="Enter a user name"
              required
            />
            <button type="submit">Create user</button>
          </form>
          <div className="list">
            {users.map((user) => (
              <article key={user.id} className="list-card">
                <div>
                  <strong>{user.name}</strong>
                </div>
                <button className="danger" onClick={() => void handleDeleteUser(user.id)}>
                  Delete
                </button>
              </article>
            ))}
            {users.length === 0 ? <p className="empty">No users yet.</p> : null}
          </div>
        </section>

        <section className="panel">
          <div className="panel-heading">
            <h2>Conversations</h2>
            <span>{conversations.length}</span>
          </div>
          <form className="stack" onSubmit={handleCreateConversation}>
            <input
              value={newConversationTitle}
              onChange={(event) => setNewConversationTitle(event.target.value)}
              placeholder="Chat title"
              required
            />
            <label className="field-label">Participants</label>
            <div className="checkbox-list">
              {users.map((user) => (
                <label key={user.id} className="checkbox-row">
                  <input
                    type="checkbox"
                    checked={selectedParticipants.includes(user.id)}
                    onChange={(event) =>
                      setSelectedParticipants((current) =>
                        event.target.checked
                          ? [...current, user.id]
                          : current.filter((id) => id !== user.id),
                      )
                    }
                  />
                  <span>{user.name}</span>
                </label>
              ))}
            </div>
            <button type="submit" disabled={selectedParticipants.length < 2}>
              Create conversation
            </button>
          </form>
          <div className="list">
            {conversations.map((conversation) => (
              <article
                key={conversation.id}
                className={`list-card selectable ${
                  activeConversationId === conversation.id ? 'active' : ''
                }`}
                onClick={() => setActiveConversationId(conversation.id)}
              >
                <div>
                  <strong>{conversation.title}</strong>
                  <p>{conversation.participants.map((user) => user.name).join(', ')}</p>
                </div>
                <button
                  className="danger"
                  onClick={(event) => {
                    event.stopPropagation()
                    void handleDeleteConversation(conversation.id)
                  }}
                >
                  Delete
                </button>
              </article>
            ))}
            {conversations.length === 0 ? (
              <p className="empty">Create at least two users to start a chat.</p>
            ) : null}
          </div>
        </section>

        <section className="panel chat-panel">
          <div className="panel-heading">
            <div>
              <h2>{activeConversation?.title ?? 'Messages'}</h2>
              <p className="muted">
                {activeConversation
                  ? activeConversation.participants.map((user) => user.name).join(', ')
                  : 'Select a conversation'}
              </p>
            </div>
          </div>

          <div className="messages">
            {loadingMessages ? <p className="empty">Loading messages...</p> : null}
            {!loadingMessages && messages.length === 0 ? (
              <p className="empty">No messages yet.</p>
            ) : null}
            {messages.map((message) => {
              const isMenuOpen = menuId === message.id
              return (
                <article 
                  key={message.id} 
                  className="message-card"
                  onMouseEnter={() => setMenuId(message.id)}
                  onMouseLeave={() => setMenuId(null)}
                >
                  <div className="message-menu">
                    <div>
                      <strong>{message.sender.name}</strong>
                      <p>{message.content}</p>
                    </div>
                    {isMenuOpen && (
                      <div className="message-menu-list">
                        <button 
                          onClick={(e) => {
                            e.stopPropagation()
                            copyToClipboard(message.content)
                          }}
                          title="Copy"
                        >
                          📋
                        </button>
                        <button 
                          className="danger small"
                          onClick={(e) => {
                            e.stopPropagation()
                            void handleDeleteMessage(message.id)
                          }}
                          title="Delete"
                        >
                          🗑️
                        </button>
                        <button 
                          onClick={(e) => {
                            e.stopPropagation()
                            setReplyTo({id: message.id, name: message.sender.name, content: message.content})
                            setNewMessage('')
                          }}
                          title="Reply"
                        >
                          💬
                        </button>
                      </div>
                    )}
                  </div>
                </article>
              )
            })}
          </div>

          <form className="stack" onSubmit={handleSendMessage}>
            <select
              value={senderId}
              onChange={(event) => setSenderId(Number(event.target.value))}
              required
              disabled={!activeConversation}
            >
              <option value="">Choose sender</option>
              {activeConversation?.participants.map((participant) => (
                <option key={participant.id} value={participant.id}>
                  {participant.name}
                </option>
              ))}
            </select>
            {replyTo && (
              <div className="reply-preview">
                <small>Replying to <strong>{replyTo.name}</strong>: {replyTo.content}</small>
                <button className="small" onClick={() => setReplyTo(null)} title="Cancel reply">✕</button>
              </div>
            )}
            <textarea
              value={newMessage}
              onChange={(event) => setNewMessage(event.target.value)}
              placeholder="Write a message..."
              rows={4}
              required
              disabled={!activeConversation}
            />
            <button type="submit" disabled={!activeConversation}>
              Send message
            </button>
          </form>
        </section>
      </main>
    </div>
  )
}

ReactDOM.createRoot(document.getElementById('app')!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)
