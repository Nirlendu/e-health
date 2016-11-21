/*
 *
 * Copyright - Nirlendu Saha
 * author - nirlendu@gmail.com
 *
 */

 /* Angular App using PouchDB */

var app = angular.module('pouch-db-example', ['pouchdb']);

app.factory('pouchdb', function() {
	return new PouchDB('sample-db');
});

app.controller('MainCtrl', ['$scope','pouchdb', function($scope, pouchdb, posts){
	$scope.test_string = 'Test String';
	$scope.posts = []
	$scope.addPost = function(user_name, post_content){
	  json_data = {_id: Date.now().toString(), user_name: user_name, post_content: post_content}
	  $scope.posts.push(json_data)
	  pouchdb.put(json_data)
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