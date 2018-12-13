var CACHE_NAME = 'my-site-cache-v1';
var urlsToCache = [
    '/',
    '/static/core/css/estilos.css',
    '/static/core/css/bootstrap-theme.css',
    '/static/core/css/bootstrap-theme.css.map',
    '/static/core/css/bootstrap-theme.min.css',
    '/static/core/css/bootstrap-theme.min.css.map',
    '/static/core/css/bootstrap.css',
    '/static/core/css/bootstrap.css.map',
    '/static/core/css/bootstrap.min.css',
    '/static/core/css/bootstrap.min.css.map',
    '/static/core/css/font-awesome.min.css',
    '/static/core/css/google.css',
    '/static/core/css/nouislider.min.css',
    '/static/core/css/slick-theme.css',
    '/static/core/css/slick.css',
    '/static/core/css/style.css',
    '/static/core/fonts/glyphicons-halflings-regular.eot',
    '/static/core/fonts/glyphicons-halflings-regular.svg',
    '/static/core/fonts/glyphicons-halflings-regular.ttf',
    '/static/core/fonts/glyphicons-halflings-regular.woff',
    '/static/core/fonts/glyphicons-halflings-regular.woff2',
    '/static/core/imagenes/hotdeal.png',
    '/static/core/imagenes/logo.png',
    '/static/core/imagenes/product01.png',
    '/static/core/imagenes/product02.png',
    '/static/core/imagenes/product05.png',
    '/static/core/imagenes/product06.png',
    '/static/core/imagenes/product07.png',
    '/static/core/imagenes/product08.png',
    '/static/core/imagenes/shop02.png',
    '/static/core/imagenes/shop03.png',
    '/static/core/imagenes/tiendaE.PNG',
    '/static/core/js/bootstrap.js',
    '/static/core/js/bootstrap.min.js',
    '/static/core/js/jQuery.js',
    '/static/core/js/jquery.zoom.min.js',
    '/static/core/js/main.js',
    '/static/core/js/nouislider.min.js',
    '/static/core/js/npm.js',
    'https://cdn.jsdelivr.net/bxslider/4.2.12/jquery.bxslider.css',
    'https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js',
    'https://cdn.jsdelivr.net/bxslider/4.2.12/jquery.bxslider.min.js',
    '/static/core/js/inicializacion.js'
];

self.addEventListener('install', function(event) {
  // Perform install steps
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(function(cache) {
        console.log('Opened cache');
        return cache.addAll(urlsToCache);
      })
  );
});

self.addEventListener('fetch', function(event){
    event.respondWith(
        caches.match(event.request).then(function(response) {
            if(response) {
                return response;
            }

            return fetch(event.request);
        })
    );
});

importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-messaging.js');

var config = {
    apiKey: "AIzaSyBHbbaRkugdwbGkAd2k_AqoW04Zu39iMFI",
    authDomain: "examendwy.firebaseapp.com",
    databaseURL: "https://examendwy.firebaseio.com",
    projectId: "examendwy",
    storageBucket: "examendwy.appspot.com",
    messagingSenderId: "399513129586"
  };
  firebase.initializeApp(config);

//agregamos un metodo que estara escuchando cuando llegue una notificacion
//incluso cuando la ventana este cerrada
const messaging = firebase.messaging();

messaging.setBackgroundMessageHandler(function(payload){

    console.log(payload);
    var tituloNotification = "titulo"
    var opciones = {
        body:'cuerpo del mensaje',
        icon:'/static/core/imagenes/logo.png'
    }
    
});

    