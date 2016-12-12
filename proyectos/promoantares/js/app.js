var App = angular.module('App', ['ui.router']);


App.config(function($stateProvider, $urlRouterProvider) {
    //
    // For any unmatched url, redirect to /state1
    $urlRouterProvider.otherwise("/home");
    //
    // Now set up the states
    $stateProvider
    .state('articulo-agricola', 
    {
      url: "/articulo/agricola",
      templateUrl: "articulo/agricola/index.html"
    })

    .state('articulo-rpi', 
    {
      url: "/articulo/rpi",
      templateUrl: "articulo/rpi/index.html"
    })

    .state('articulo-cerdigres', 
    {
      url: "/articulo/cerdigres",
      templateUrl: "articulo/cerdigres/index.html"
    })

    .state('articulo-amigo', 
    {
      url: "/articulo/amigo",
      templateUrl: "articulo/amigo/index.html"
    })

    .state('articulo-cerdigres-media', 
    {
      url: "/articulo/cerdigres/media",
      templateUrl: "articulo/cerdigres/media.html"
    })

    .state('home', 
    {
      url: "/home",
      templateUrl: "home.html"
    })
});