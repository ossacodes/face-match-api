const fetchTweets = async () => {};

// login with firebase and get the user's data
const login = async () => {
  const provider = new firebase.auth.GoogleAuthProvider();
  const result = await firebase.auth().signInWithPopup(provider);
  return result.user;
};
