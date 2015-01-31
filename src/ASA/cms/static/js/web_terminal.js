var app = angular.module("web_terminal", []).config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
});
		app.controller("f", function($scope, $http){
			$scope.user = "ASA.tv";
			$scope.host = "psycium.xyz";
			$scope.pwd = "\\";
			$scope.coms = [];
			$scope.inp = "";
			
			$scope.submit = function(){
				/*TODO:retieve data from server
				*/
				$scope.oup = "msg has been sent";
				$scope.coms.push({inp:$scope.inp, oup:$scope.oup});
				$scope.inp = "";
			}
		});