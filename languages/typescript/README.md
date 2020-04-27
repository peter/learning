# TypeScript

Notes in learning Typescript

## Installation

```sh
npm install -g typescript
```

## Recommended IDE/Editor

Visual Studio Code

## Project Configuration

Create a sample tsconfig.json file and edit it:

```sh
tsc --init
```

## Node Configuration

Example `tsconfig.json` for Node (also see [tsconfig.json](https://github.com/microsoft/TypeScript-Node-Starter/blob/master/tsconfig.json) in the TypeScript Node Starter app):

```json
{
  "compilerOptions": {
    "module": "commonjs",
    "esModuleInterop": true,
    "target": "ES2019",
    "outDir": "dist",
    "baseUrl": ".",
    "scrict": true,
    "moduleResolution": "node",
    "sourceMap": true,
    "noImplicitAny": true,
    "strictNullChecks": true
  },
  "include": [
    "src/**/*.ts"
  ]
}
```

Example scripts in package.json:

```json
{
  "scripts": {
    "start": "node dist/server.js",
    "dev": "nodemon dist/server.js",
    "test": "jest",
    "test-watch": "npm run test -- --watchAll",
    "build": "tsc",
    "build-watch": "tsc -w",
    "tslint": "tslint -c tslint.json -p tsconfig.json"
  }
}
```

An alternative to Nodemon for hot-reloading is [ts-node-dev](https://www.npmjs.com/package/ts-node-dev)

## Migration from JavaScript

Example script to change extension of source files:

```sh
for file in $(find src -iname '*.js'); do git mv "$file" "${file%.js}.ts"; done
```

You may want to change your code from using Node modules (requires) to using ES6 modules (imports).

## Reousrces

Official [TypeScript Documentation](https://www.typescriptlang.org/docs/home.html):

* [TypeScript in 5 minutes](https://www.typescriptlang.org/docs/handbook/typescript-in-5-minutes.html)
* [TypeScript Project Configuration (tsconfig.json)](https://www.typescriptlang.org/docs/handbook/tsconfig-json.html)
* [Handbook - Basic Types](https://www.typescriptlang.org/docs/handbook/basic-types.html)

* [TypeScript Example/Starter Projects (React, Express, Migration Guide etc.)](https://www.typescriptlang.org/Samples)
