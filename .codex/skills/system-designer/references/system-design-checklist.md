# System Design Checklist

Use this checklist when designing any system.

## 1. Clarify Requirements

- What problem are we solving?
- Who are the users?
- What are the core features?
- What scale is expected (users, requests, data)?

## 2. Define System Scope

- Is this MVP or production-ready?
- What parts are in scope (frontend, backend, database, infra)?

## 3. High-Level Architecture

- Define main components:
  - Client (web/mobile)
  - Backend (API/services)
  - Database
  - External services

## 4. Data Flow

- How does data move through the system?
- What are the key APIs and interactions?

## 5. Database Design

- What type (SQL / NoSQL)?
- Main entities and relationships
- Indexes and performance considerations

## 6. Scalability

- How will the system handle growth?
- Load balancing
- Horizontal vs vertical scaling
- Caching strategies

## 7. Reliability & Fault Tolerance

- What happens if a service fails?
- Retries, backups, redundancy

## 8. Security

- Authentication & authorization
- Data protection
- Rate limiting

## 9. Trade-offs

- What decisions were made and why?
- What are the limitations?

## 10. Summary

- Provide a simple, clear architecture explanation