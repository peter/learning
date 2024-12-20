# Firebase

From [Wikipedia](https://en.wikipedia.org/wiki/Firebase):

"Firebase is a mobile and web application development platform developed by Firebase, Inc. in 2011, then acquired by Google in 2014. As of October 2018, the Firebase platform has 18 products,[6] which are used by 1.5 million apps"

"In October 2017, Firebase launched Cloud Firestore, a realtime document database as the successor product to the original Firebase Realtime Database"

The origins of Firebase is an online chat application developed in 2011.

Prior to the Firestore database "Firebase’s largest customers often hit the service’s hard limit of 100,000 concurrently connected devices and had to split their databases across shards".

## Firebase with React (Frontend Masters Course)

Instructor: https://twitter.com/stevekinney

```bash
npm install -g create-react-app
npm install -g firebase-tools
```

Repo: https://github.com/stevekinney/think-piece

## Creating and Deploying a Firebase App with the CLI

```
npm install -g firebase-tools
firebase login
mkdir my-firebase-project && cd my-firebase-project
firebase init hosting # creates firebase.json and index.html
firebase serve # open http://localhost:5000
firebase deploy # deploys app to a public URL with https
```

## Authentication

TODO, see: https://angularfirebase.com/lessons/the-ultimate-beginners-guide-to-firebase/

## Listening for Realtime Database Updates

TODO: see https://angularfirebase.com/lessons/the-ultimate-beginners-guide-to-firebase/

## File Storage

TODO, see: ## Listening for Realtime Database Updates

TODO: see https://angularfirebase.com/lessons/the-ultimate-beginners-guide-to-firebase/

## Cloud Functions (Node.js Backend Code)

TODO, see: https://angularfirebase.com/lessons/the-ultimate-beginners-guide-to-firebase/

```
firebase init functions
```

## Resources

* [Firebase with React (Frontend Masters Course)](https://frontendmasters.com/courses/firebase-react-v2/)
* [Firebase - Ultimate Beginner's Guide (Youtube Video)](https://www.youtube.com/watch?v=9kRgVxULbag)
* [Heroku Alternatives](https://blog.back4app.com/2018/03/13/heroku-alternatives/)
