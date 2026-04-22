import { PrismaClient } from '@prisma/client';
import { PrismaPg } from '@prisma/adapter-pg';
import pg from 'pg';
import dotenv from 'dotenv';

dotenv.config();

const pool = new pg.Pool({
  connectionString: process.env.DATABASE_URL,
});

const adapter = new PrismaPg(pool);
const prisma = new PrismaClient({ adapter });

export interface TaskFilter {
  status?: string;
  priority?: string;
  search?: string;
  sortBy?: 'createdAt' | 'dueDate' | 'priority';
  order?: 'asc' | 'desc';
  limit?: number;
  offset?: number;
}

export class TaskRepository {
  async create(data: {
    title: string;
    description?: string | null;
    status?: string;
    priority?: string;
    dueDate?: Date | null;
  }) {
    return prisma.task.create({
      data: {
        title: data.title,
        description: data.description,
        status: data.status as any,
        priority: data.priority as any,
        dueDate: data.dueDate,
      },
    });
  }

  async findById(id: string) {
    return prisma.task.findUnique({
      where: { id },
    });
  }

  async findAll(filter: TaskFilter) {
    const {
      status,
      priority,
      search,
      sortBy = 'createdAt',
      order = 'desc',
      limit = 20,
      offset = 0,
    } = filter;

    const where: any = {};
    if (status) where.status = status;
    if (priority) where.priority = priority;
    if (search) {
      where.OR = [
        { title: { contains: search, mode: 'insensitive' } },
        { description: { contains: search, mode: 'insensitive' } },
      ];
    }

    return prisma.task.findMany({
      where,
      orderBy: { [sortBy]: order },
      take: limit,
      skip: offset,
    });
  }

  async update(id: string, data: any) {
    return prisma.task.update({
      where: { id },
      data,
    });
  }

  async delete(id: string) {
    return prisma.task.delete({
      where: { id },
    });
  }

  async deleteMany() {
    return prisma.task.deleteMany();
  }
}

export const taskRepository = new TaskRepository();
