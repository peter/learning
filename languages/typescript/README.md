# TypeScript

Notes in learning Typescript

## Install

```sh
npm install -g typescript
```

## Hello World

```sh
cd examples
tsc hello_world.ts
node hello_world.js
```

## Recommended IDE/Editor

Visual Studio Code with these extensions:

* TSLint

## Configuring TypesScript with Node.js

Add typescript and any relevant types to your project:

```sh
yarn add -D typescript
yarn add -D @types/node
yarn add -D @types/jest
```

TypeScript support for Jest:

```sh
yarn add -D ts-jest
```

Add linting with the Standard style:

```sh
yarn add -D tslint
yarn add -D tslint-config-standard
```

Run `tsc --init` to generate a `tsconfig.json` file and edit it:

```json
{
  "compilerOptions": {
    "target": "es6",
    "module": "commonjs",
    "outDir": "dist",
    "esModuleInterop": true,
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

Example script to change extension of source files:

```sh
for file in $(find src -iname '*.js'); do git mv "$file" "${file%.js}.ts"; done
```

You may want to change your code from using Node modules (requires) to using ES6 modules (imports).

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

## Resources

* [TypeScript in 5 minutes](https://www.typescriptlang.org/docs/handbook/typescript-in-5-minutes.html)
* [TypeScript Official Examples](https://www.typescriptlang.org/samples)
* [TypeScript Basic Types](https://www.typescriptlang.org/docs/handbook/basic-types.html)
