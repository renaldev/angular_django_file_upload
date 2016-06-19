'use strict';

var graphsApp = angular.module('graphsApp', [
    'ngCookies',
    'zingchart-angularjs',
    'graphsControllers',
    'graphsDirectives',
    'graphsServices'

]);

graphsApp.config(['$httpProvider', '$interpolateProvider', function($httpProvider, $interpolateProvider) {
    $httpProvider.defaults.headers.post['X-CSRFToken'] = $('input[name=csrfmiddlewaretoken]').val();
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
}]);