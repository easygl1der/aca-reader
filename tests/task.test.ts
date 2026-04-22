import { describe, it, expect, beforeEach } from 'vitest';
import { taskService } from '../src/services/task.service.js';
import { taskRepository } from '../src/repositories/task.repository.js';
import { Status } from '@prisma/client';

describe('Task Service Integration', () => {
  beforeEach(async () => {
    // Clear the database before each test
    await taskRepository.deleteMany();
  });

  it('should create a task', async () => {
    const task = await taskService.createTask({
      title: 'Test Task',
      description: 'Test Description',
      priority: 'High',
    });
    expect(task.title).toBe('Test Task');
    expect(task.status).toBe(Status.Todo);
  });

  it('should handle valid status transitions', async () => {
    const task = await taskService.createTask({ title: 'Transition Task' });

    // Todo -> InProgress
    await taskService.updateTask(task.id, { status: Status.InProgress });
    let updated = await taskService.getTask(task.id);
    expect(updated.status).toBe(Status.InProgress);

    // InProgress -> Review
    await taskService.updateTask(task.id, { status: Status.Review });
    updated = await taskService.getTask(task.id);
    expect(updated.status).toBe(Status.Review);

    // Review -> Done
    await taskService.updateTask(task.id, { status: Status.Done });
    updated = await taskService.getTask(task.id);
    expect(updated.status).toBe(Status.Done);
  });

  it('should block invalid status transitions', async () => {
    const task = await taskService.createTask({ title: 'Invalid Transition Task' });

    // Todo -> Done (Invalid)
    await expect(taskService.updateTask(task.id, { status: Status.Done }))
      .rejects.toThrow('Invalid status transition from Todo to Done');
  });

  describe('Edge Case Stress Tests', () => {
    it('should handle extreme input (long strings)', async () => {
      const longTitle = 'a'.repeat(10000);
      const longDesc = 'b'.repeat(10000);
      const task = await taskService.createTask({
        title: longTitle,
        description: longDesc,
      });
      expect(task.title).toBe(longTitle);
      expect(task.description).toBe(longDesc);
    });

    it('should handle empty fields', async () => {
      const task = await taskService.createTask({
        title: 'Minimal Task',
        description: '',
      });
      expect(task.title).toBe('Minimal Task');
      expect(task.description).toBe('');
    });

    it('should return 404 for non-existent ID', async () => {
      await expect(taskService.getTask('non-existent-id'))
        .rejects.toThrow('Task not found');
    });

    it('should handle pagination boundaries', async () => {
      // Create 5 tasks
      for (let i = 0; i < 5; i++) {
        await taskService.createTask({ title: `Task ${i}` });
      }

      // Request page 100 (offset 2000, limit 20)
      const tasks = await taskService.listTasks({
        limit: 20,
        offset: 2000,
      });
      expect(tasks.length).toBe(0);
    });

    it('should handle search with no results', async () => {
      await taskService.createTask({ title: 'Actual Task' });
      const tasks = await taskService.listTasks({ search: 'Non-existent' });
      expect(tasks.length).toBe(0);
    });
  });
});

