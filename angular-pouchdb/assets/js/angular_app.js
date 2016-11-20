/*
 *
 * Copyright - Nirlendu Saha
 * author - nirlendu@gmail.com
 *
 */

 // Angular App

var app = angular.module('pouch-db-example', ['pouchdb']);

app.factory('pouchdb', function() {
	return new PouchDB('sample-db');
});

app.controller('MainCtrl', ['$scope','pouchdb', function($scope, pouchdb, posts){
	$scope.test_string = 'Test String';
	$scope.posts = []
	$scope.addPost = function(){
	  $scope.posts.push({title: 'A new post!', upvotes: 0});
	  pouchdb.put({_id: Date.now().toString(), title: 'A new post!', upvotes: 0})
		.then(get)
		.catch(error);
	};

	function error(err) {
		alert(err);
	}

	function get(res) {
		if (!res.ok) {
			return error(res);
		}
		return pouchdb.get(res.id);
	}

}]);