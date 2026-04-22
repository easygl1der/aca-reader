import { z } from 'zod';

export const TaskCreateInput = z.object({
  title: z.string().min(1),
  description: z.string().nullable().optional(),
  priority: z.enum(['Low', 'Medium', 'High', 'Urgent']).optional().default('Medium'),
  dueDate: z.string().datetime().nullable().optional(),
});

export const TaskUpdateInput = z.object({
  title: z.string().min(1).optional(),
  description: z.string().nullable().optional(),
  status: z.enum(['Todo', 'InProgress', 'Review', 'Done']).optional(),
  priority: z.enum(['Low', 'Medium', 'High', 'Urgent']).optional(),
  dueDate: z.string().datetime().nullable().optional(),
});

export const TaskQuery = z.object({
  status: z.enum(['Todo', 'InProgress', 'Review', 'Done']).optional(),
  priority: z.enum(['Low', 'Medium', 'High', 'Urgent']).optional(),
  search: z.string().optional(),
  sortBy: z.enum(['createdAt', 'dueDate', 'priority']).optional().default('createdAt'),
  order: z.enum(['asc', 'desc']).optional().default('desc'),
  limit: z.number().int().min(1).max(100).optional().default(20),
  offset: z.number().int().min(0).optional().default(0),
});
