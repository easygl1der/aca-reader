import { taskRepository, TaskFilter } from '../repositories/task.repository.js';
import { Status, Priority } from '@prisma/client';

export class TaskService {
  private static readonly VALID_TRANSITIONS: Record<Status, Status[]> = {
    [Status.Todo]: [Status.InProgress, Status.Todo],
    [Status.InProgress]: [Status.Review, Status.Todo, Status.InProgress],
    [Status.Review]: [Status.Done, Status.InProgress, Status.Review],
    [Status.Done]: [Status.Todo, Status.Done], // Allow resetting to Todo
  };

  async createTask(data: any) {
    return taskRepository.create(data);
  }

  async getTask(id: string) {
    const task = await taskRepository.findById(id);
    if (!task) throw new Error('Task not found');
    return task;
  }

  async listTasks(filter: TaskFilter) {
    return taskRepository.findAll(filter);
  }

  async updateTask(id: string, updates: any) {
    const currentTask = await this.getTask(id);

    if (updates.status) {
      const currentStatus = currentTask.status as Status;
      const newStatus = updates.status as Status;

      if (!TaskService.VALID_TRANSITIONS[currentStatus].includes(newStatus)) {
        throw new Error(`Invalid status transition from ${currentStatus} to ${newStatus}`);
      }
    }

    return taskRepository.update(id, updates);
  }

  async deleteTask(id: string) {
    return taskRepository.delete(id);
  }
}

export const taskService = new TaskService();
