---
name: system-designer
description: Design scalable, reliable, and maintainable system architectures. Use when Codex is asked to design applications, define system components, create architecture diagrams, plan backend/frontend structure, or make technical design decisions for real-world systems.
---

# System Designer

## Overview

Use this skill when the task is to design a system architecture, not just describe technologies.

Start by reading [references/system-design-checklist.md](references/system-design-checklist.md). Use it as the default framework, then adapt based on system complexity, scale, and requirements.

## Workflow

1. Clarify requirements.
Identify the problem, users, core features, expected scale, and constraints.

2. Define system scope.
Determine whether the system is MVP-level or production-ready and which components are included.

3. Design high-level architecture.
Break the system into major components such as client, backend services, database, and external integrations.

4. Define data flow.
Describe how data moves through the system from user interaction to storage and response.

5. Design the database.
Choose appropriate storage (SQL/NoSQL) and define key entities, relationships, and access patterns.

6. Plan for scalability.
Consider load balancing, horizontal scaling, caching strategies, and performance bottlenecks.

7. Ensure reliability.
Add fault tolerance, retries, backups, and redundancy where needed.

8. Address security.
Define authentication, authorization, data protection, and access control strategies.

9. Evaluate trade-offs.
Explain key decisions, alternatives considered, and system limitations.

## System Design Guidance

- Prefer simple architectures first, then scale complexity only when needed.
- Clearly separate responsibilities between components.
- Treat backend as the source of truth for data and logic.
- Avoid overengineering for small or low-scale systems.
- Consider real-world constraints such as latency, cost, and maintainability.

## Common Design Scenarios

### Web Applications

- Frontend (React, Angular, etc.)
- Backend API (Node.js, .NET, etc.)
- Database (SQL or NoSQL)
- Optional caching and CDN

### Scalable Systems

- Load balancer in front of services
- Stateless backend services
- Distributed databases or replicas
- Caching layer (Redis)

### Data-Driven Systems

- Data ingestion pipelines
- Storage (data warehouse or database)
- Processing and analytics layers

## Response Shape

Default to a structured design output:

1. Problem definition  
2. Architecture overview  
3. Components and responsibilities  
4. Data flow  
5. Database design  
6. Scalability considerations  
7. Security considerations  
8. Trade-offs  

Keep explanations clear, structured, and aligned with real-world systems.