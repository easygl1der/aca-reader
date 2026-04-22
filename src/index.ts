import Fastify from 'fastify';
import fastifySwagger from '@fastify/swagger';
import fastifySwaggerUi from '@fastify/swagger-ui';
import { taskRoutes } from './routes/task.routes.js';

const fastify = Fastify({
  logger: true,
});

async function bootstrap() {
  await fastify.register(fastifySwagger, {
    openapi: {
      info: {
        title: 'Task Management API',
        version: '1.0.0',
        description: 'API for managing tasks and their lifecycles',
      },
    },
  });

  await fastify.register(fastifySwaggerUi);

  await fastify.register(taskRoutes);

  try {
    await fastify.listen({ port: 3000, host: '0.0.0.0' });
    console.log('Server listening on http://0.0.0.0:3000');
  } catch (err) {
    console.error(err);
    process.exit(1);
  }
}

bootstrap();
