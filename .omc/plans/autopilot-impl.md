# Implementation Plan: Task Management REST API (Autopilot)

This document outlines the step-by-step implementation of the Task Management REST API as specified in `.omc/autopilot/spec.md`.

## 1. Implementation Strategy
The project will follow a layered architecture:
- **Route Layer**: Handles HTTP requests/responses and Zod validation.
- **Service Layer**: Contains business logic (e.g., state machine transitions).
- **Repository Layer**: Prisma-based database access.
- **Data Layer**: PostgreSQL.

## 2. Atomic Task Breakdown

### Phase 1: Project Initialization & Infrastructure
- [ ] **Task 1.1: Project Setup**
    - Initialize Node.js project: `npm init -y`
    - Setup TypeScript: `npm install typescript ts-node @types/node --save-dev`
    - Configure `tsconfig.json` for ESM and Node 20+.
    - Create project structure: `src/`, `src/routes`, `src/services`, `src/repositories`, `prisma/`.
    - **Verification**: Run `npx tsc` and ensure no configuration errors.
- [ ] **Task 1.2: Dependency Installation**
    - Install core dependencies: `npm install fastify zod @prisma/client`
    - Install dev dependencies: `npm install prisma fastify-swagger @fastify/swagger @fastify/swagger-ui --save-dev`
    - **Verification**: Check `package.json` for all required packages.
- [ ] **Task 1.3: Database Schema & Migration**
    - Initialize Prisma: `npx prisma init`
    - Implement `Task`, `Status`, and `Priority` models in `prisma/schema.prisma` per spec.
    - Run initial migration: `npx prisma migrate dev --name init`
    - **Verification**: Use `npx prisma studio` to verify the table structure exists in PostgreSQL.

### Phase 2: Repository & Service Layers (Core Logic)
- [ ] **Task 2.1: Task Repository**
    - Create `src/repositories/task.repository.ts` with methods: `create`, `findById`, `findAll` (with filters/pagination), `update`, `delete`.
    - **Verification**: Write a small standalone script to test DB CRUD via the repository.
- [ ] **Task 2.2: Task Service & State Machine**
    - Create `src/services/task.service.ts`.
    - Implement state transition logic: `Todo` $\rightarrow$ `InProgress` $\rightarrow$ `Review` $\rightarrow$ `Done`.
    - Implement validation for updating priority and due dates.
    - **Verification**: Unit test the `updateStatus` method with valid and invalid transitions.

### Phase 3: API Route Implementation
- [ ] **Task 3.1: Request/Response Validation (Zod)**
    - Define `TaskCreateInput`, `TaskUpdateInput`, and `TaskQuery` schemas in `src/routes/schemas.ts`.
    - **Verification**: Test schemas against mock JSON objects.
- [ ] **Task 3.2: Create & Read Endpoints**
    - Implement `POST /tasks` and `GET /tasks` (including filtering/pagination).
    - Implement `GET /tasks/:id`.
    - **Verification**: Use `curl` or Postman to verify:
        - `POST /tasks` returns 201 and created task.
        - `GET /tasks` returns paginated list.
        - `GET /tasks/:id` returns 200 for existing, 404 for non-existent.
- [ ] **Task 3.3: Update & Delete Endpoints**
    - Implement `PATCH /tasks/:id` (calling Task Service for state validation).
    - Implement `DELETE /tasks/:id`.
    - **Verification**: 
        - Verify `PATCH` prevents invalid status jumps (e.g., `Todo` $\rightarrow$ `Done` directly).
        - Verify `DELETE` returns 204 on success.

### Phase 4: Documentation & Final Polish
- [ ] **Task 4.1: Swagger Integration**
    - Configure `@fastify/swagger` and `@fastify/swagger-ui`.
    - Add OpenAPI 3.0 descriptions to routes.
    - **Verification**: Access `/docs` and verify all endpoints and schemas are documented.
- [ ] **Task 4.2: Integration Testing**
    - Create a test suite using `vitest` or `jest`.
    - Test the full "Task Lifecycle" (Create $\rightarrow$ InProgress $\rightarrow$ Review $\rightarrow$ Done).
    - **Verification**: All tests pass in CI/local environment.

## 3. Execution Sequence & Parallelism

| Sequence | Tasks | Dependency | Parallelizable? |
| :--- | :--- | :--- | :--- |
| 1 | 1.1 $\rightarrow$ 1.2 $\rightarrow$ 1.3 | None | No |
| 2 | 2.1 $\rightarrow$ 2.2 | 1.3 | No |
| 3 | 3.1 $\rightarrow$ (3.2 $\parallel$ 3.3) | 2.2 | Yes (3.2 and 3.3) |
| 4 | 4.1 $\rightarrow$ 4.2 | 3.3 | No |

## 4. Edge Cases & Error Handling (Critic Review Points)
- **Invalid Transitions**: If a user tries to move a task from `Todo` to `Done` without `InProgress`, the API must return `400 Bad Request`.
- **Pagination Limits**: Ensure `limit` has a maximum value (e.g., 100) to prevent DoS.
- **Non-existent IDs**: All `:id` endpoints must handle 404s gracefully.
- **Database Downtime**: Implement basic try-catch blocks in the repository layer to return `500 Internal Server Error`.
- **Date Validation**: Ensure `dueDate` is a valid ISO8601 date and not in the past for new tasks (optional but recommended).
