import firebase from 'firebase/app';
import 'firebase/firestore';

const config = {
  apiKey: 'AIzaSyAdiINL-a4cg_Aps8zWyPB3MMbB2SdEA6s',
  authDomain: 'frontendmasters-course.firebaseapp.com',
  databaseURL: 'https://frontendmasters-course.firebaseio.com',
  projectId: 'frontendmasters-course',
  storageBucket: 'frontendmasters-course.appspot.com',
  messagingSenderId: '98218894562',
};

firebase.initializeApp(config);

export const firestore = firebase.firestore();

export default firebase;
