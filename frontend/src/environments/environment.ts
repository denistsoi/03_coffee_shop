export const environment = {
  production: false,
  apiServerUrl: "http://127.0.0.1:5000", // the running FLASK api server url
  auth0: {
    url: "dev-98w9-5eh", // the auth0 domain prefix
    audience: "coffee-shop", // the audience set for the auth0 app
    clientId: "k9qCxdNpbDS36iGzKL7cSdd44KnFVhiq", // the client id generated for the auth0 app
    callbackURL: "http://localhost:4200", // the base url of the running ionic application.
  },
};
