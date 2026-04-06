# Message Options (Copy/Delete/Reply) Implementation TODO

## Steps:
- [x] 1. Update frontend/src/main.tsx: Add menu state (menuId, replyTo), copy func, reply logic (prepend to textarea), update render for menu + reply indicator, adjust handleSendMessage.
- [x] 2. Update frontend/src/style.css: Add styles for .message-options, .message-menu, hover effects, popup positioning.
- [ ] 3. Test: `cd frontend && npm run dev` (backend also if needed), verify hover menu, copy to clipboard, reply prepends, delete works, send clears reply.
- [ ] 4. Complete: Remove this TODO.md.

Progress: Styles added. Feature complete! Ready for testing.

