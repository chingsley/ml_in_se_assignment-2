from DeepSeek import Deepseek
from CodeLlama import CodeLlama

promptTxt = """
router.get('/pending', authenticateToken, getPendingQuestions);

export const _ = async (req: Request, res: Response) => {
  try {
    const { questionIds } = req.query;

    if (!questionIds) {
      return res.status(400).json({ error: 'No questionIds provided' });
    }

    const parsedIds = (questionIds as string).split(',').map(id => id.trim());
    const question = await prisma.question.findMany({
      where: {
        id: {
          in: parsedIds
        },
      },
      include: {
        user: {
          select: {
            username: true, // Include the question creator's username
          },
        },
      },
    });

    return res.json(question);
  } catch (error) {
    // console.log("\n>>>>>> error: ", error, "\n");
    return res.status(500).json({ error: 'Failed to get question. Internal server error.' });
  }
};

const JWT_SECRET = process.env.JWT_SECRET || 'your_jwt_secret';

export const authenticateToken = (req: Request, res: Response, next: NextFunction) => {
  const token = req.header('Authorization')?.replace('Bearer ', '');

  if (!token) return res.status(401).json({ error: 'Access denied, no token provided' });

  try {
    const decoded = jwt.verify(token, JWT_SECRET) as TokenPayload;
    req.user = decoded;
    next();
  } catch (err) {
    res.status(401).json({ error: 'Invalid token' });
  }
};

{
  "name": "my_project",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "directories": {
    "test": "tests"
  },
  "scripts": {
    "start:queues": "ts-node src/core/queues/index.ts",
    "start": "ts-node src/index.ts",
    "dev": "concurrently \"redis-server\" \"nodemon src/index.ts\" \"npm run start:queues\"",
    "build": "tsc",
    "undo:migrate": "prisma migrate reset --force --schema src/core/database/prisma/schema.prisma",
    "migrate": "prisma migrate dev --name init --schema src/core/database/prisma/schema.prisma",
    "seed": "ts-node src/core/database/seeders/seed.ts",
    "db:reset:dev": "npm run undo:migrate && npm run migrate && npm run seed",
    "migrate:init:test": "dotenv -e .env.test -- prisma migrate deploy --schema=src/core/database/prisma/schema.prisma",
    "migrate:reset:test": "dotenv -e .env.test -- prisma migrate reset --force --schema=src/core/database/prisma/schema.prisma",
    "test": "NODE_ENV=test && jest --watchAll --detectOpenHandles",
    "test:module:question": "NODE_ENV=test && jest tests/modules/question/questions.test.ts --detectOpenHandles --verbose --watch",
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "@faker-js/faker": "^8.0.0",
    "@types/bcrypt": "^5.0.2",
    "@types/bull": "^4.10.0",
    "@types/cors": "^2.8.17",
    "@types/express": "^4.17.21",
    "@types/jest": "^29.5.14",
    "@types/joi": "^17.2.3",
    "@types/jsonwebtoken": "^9.0.6",
    "@types/node": "^22.4.0",
    "@types/supertest": "^6.0.2",
    "@types/uuid": "^10.0.0",
    "concurrently": "^8.2.2",
    "dotenv-cli": "^7.4.2",
    "express": "^4.19.2",
    "jest": "^29.7.0",
    "nodemon": "^3.1.4",
    "supertest": "^7.0.0",
    "ts-jest": "^29.2.5",
    "ts-node": "^10.9.2",
    "typescript": "^5.5.4"
  },
  "dependencies": {
    "@prisma/client": "^5.19.1",
    "bcrypt": "^5.1.1",
    "bull": "^4.16.0",
    "cors": "^2.8.5",
    "joi": "^17.13.3",
    "jsonwebtoken": "^9.0.2",
    "pg": "^8.12.0",
    "prisma": "^5.19.1",
    "uuid": "^10.0.0"
  }
}

generate unit tests that will ensure this endpoint is fail proof
"""


model = Deepseek()
# model = CodeLlama()
response = model.prompt(promptTxt)
print(response)
