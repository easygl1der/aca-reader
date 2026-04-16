# Technical Specification: Task Management REST API

## 1. Functional Requirements

### 1.1 Core CRUD Operations
- **Create Task**: Create a new task with a title, description, and optional priority/due date.
- **Read Task**: Retrieve a single task by ID or a list of tasks.
- **Update Task**: Modify task details, including title, description, status, and priority.
- **Delete Task**: Remove a task from the system.

### 1.2 Task Lifecycle & State Management
- **Status Transitions**: Tasks must follow a logical state machine:
  - `Todo` $\rightarrow$ `In Progress` $\rightarrow$ `Review` $\rightarrow$ `Done`
  - Tasks can be moved back to `Todo` from `In Progress` or `Review`.
- **Priority Levels**: `Low`, `Medium`, `High`, `Urgent`.
- **Due Dates**: Support for setting and tracking deadlines.

### 1.3 Filtering and Sorting
- **Filtering**: Ability to filter tasks by status, priority, and search keywords (title/description).
- **Sorting**: Sort by creation date, due date, or priority.
- **Pagination**: Implement offset-based or cursor-based pagination for list endpoints to ensure scalability.

### 1.4 Advanced Features (Optional/Future)
- **User Assignment**: Assign tasks to specific users.
- **Tags/Labels**: Add custom tags for categorization.
- **Audit Log**: Track changes to task status and metadata.

---

## 2. Technical Stack

### 2.1 Recommended Stack: Node.js + TypeScript + PostgreSQL
- **Language**: TypeScript (for type safety and maintainable API contracts).
- **Framework**: Fastify or Express (Fastify preferred for performance and built-in schema validation).
- **Database**: PostgreSQL (relational structure is ideal for tasks, statuses, and future user relations).
- **ORM**: Prisma (provides type-safe database access and easy migrations).
- **Validation**: Zod (for request body and query parameter validation).
- **Documentation**: Swagger/OpenAPI 3.0.

### 2.2 Rationale
- **TypeScript**: Ensures that the API surface is well-defined and reduces runtime errors.
- **PostgreSQL**: Handles complex queries and filtering efficiently.
- **Prisma**: Accelerates development with a strong schema-first approach.

---

## 3. API Design (REST)

### 3.1 Base URL
`/api/v1`

### 3.2 Endpoints

| Method | Endpoint | Description | Request Schema | Response Schema |
| :--- | :--- | :--- | :--- | :--- |
| `POST` | `/tasks` | Create a task | `TaskCreateInput` | `Task` |
| `GET` | `/tasks` | List tasks (filtered) | `TaskQuery` | `PaginatedTasks` |
| `GET` | `/tasks/:id` | Get task details | N/A | `Task` |
| `PATCH` | `/tasks/:id` | Update task | `TaskUpdateInput` | `Task` |
| `DELETE` | `/tasks/:id` | Delete a task | N/A | `Empty` |

### 3.3 Schemas

#### `Task` (Data Model)
```typescript
{
  id: string; // UUID
  title: string;
  description: string | null;
  status: 'Todo' | 'InProgress' | 'Review' | 'Done';
  priority: 'Low' | 'Medium' | 'High' | 'Urgent';
  dueDate: ISO8601Date | null;
  createdAt: ISO8601Date;
  updatedAt: ISO8601Date;
}
```

#### `TaskQuery` (Filtering/Sorting)
- `status`: Optional string.
- `priority`: Optional string.
- `search`: Optional keyword search.
- `sortBy`: `createdAt` | `dueDate` | `priority`.
- `order`: `asc` | `desc`.
- `limit`: Number (default 20).
- `offset`: Number (default 0).

---

## 4. Data Model

### 4.1 Database Schema (Prisma Notation)
```prisma
model Task {
  id          String   @id @default(uuid())
  title       String
  description String?
  status      Status   @default(Todo)
  priority    Priority @default(Medium)
  dueDate     DateTime?
  createdAt   DateTime @default(now())
  updatedAt   DateTime @updatedAt

  @@index([status])
  @@index([priority])
}

enum Status {
  Todo
  InProgress
  Review
  Done
}

enum Priority {
  Low
  Medium
  High
  Urgent
}
```

## 5. Implementation Plan for Executor

1. **Project Initialization**:
   - Initialize Node.js project with TypeScript.
   - Install dependencies: `fastify`, `prisma`, `@prisma/client`, `zod`.
2. **Database Setup**:
   - Configure PostgreSQL connection.
   - Run `prisma migrate dev` to create the `Task` table.
3. **Route Implementation**:
   - Implement `POST /tasks` with Zod validation.
   - Implement `GET /tasks` with Prisma filtering and pagination.
   - Implement `GET /tasks/:id` and `PATCH /tasks/:id` (including status transition validation).
   - Implement `DELETE /tasks/:id`.
4. **Validation & Testing**:
   - Unit tests for status transition logic.
   - Integration tests for all REST endpoints.
5. **Documentation**:
   - Generate Swagger UI using `fastify-swagger`.
