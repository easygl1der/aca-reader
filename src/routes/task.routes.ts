import Fastify, { FastifyInstance, FastifyRequest, FastifyReply } from 'fastify';
import { taskService } from '../services/task.service.js';
import { TaskCreateInput, TaskUpdateInput, TaskQuery } from './schemas.js';

export async function taskRoutes(fastify: FastifyInstance) {
  fastify.post('/tasks', {
    schema: {
      body: TaskCreateInput,
    },
    handler: async (request: FastifyRequest<{ Body: any }>, reply: FastifyReply) => {
      const data = TaskCreateInput.parse(request.body);
      const task = await taskService.createTask(data);
      return reply.code(201).send(task);
    },
  });

  fastify.get('/tasks', {
    schema: {
      querystring: TaskQuery,
    },
    handler: async (request: FastifyRequest<{ Querystring: any }>, reply: FastifyReply) => {
      const query = TaskQuery.parse(request.query);
      const tasks = await taskService.listTasks(query);
      return tasks;
    },
  });

  fastify.get('/tasks/:id', {
    handler: async (request: FastifyRequest<{ Params: { id: string } }>, reply: FastifyReply) => {
      const { id } = request.params;
      try {
        return await taskService.getTask(id);
      } catch (e: any) {
        return reply.code(404).send({ error: 'Task not found' });
      }
    },
  });

  fastify.patch('/tasks/:id', {
    schema: {
      body: TaskUpdateInput,
    },
    handler: async (request: FastifyRequest<{ Params: { id: string }, Body: any }>, reply: FastifyReply) => {
      const { id } = request.params;
      const data = TaskUpdateInput.parse(request.body);
      try {
        return await taskService.updateTask(id, data);
      } catch (e: any) {
        if (e.message.includes('Invalid status transition')) {
          return reply.code(400).send({ error: e.message });
        }
        return reply.code(404).send({ error: e.message });
      }
    },
  });

  fastify.delete('/tasks/:id', {
    handler: async (request: FastifyRequest<{ Params: { id: string } }>, reply: FastifyReply) => {
      const { id } = request.params;
      try {
        await taskService.deleteTask(id);
        return reply.code(204).send();
      } catch (e: any) {
        return reply.code(404).send({ error: 'Task not found' });
      }
    },
  });
}
