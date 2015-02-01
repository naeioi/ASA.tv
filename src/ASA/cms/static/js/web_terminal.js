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
			
			//$http.get("../cms/.");

			$scope.submit = function(){
				$http.get("../cms/" + encodeURI($scope.inp)).
					success(function(data, status, headers, config){
						$scope.oup = status == 200 ? data.msg : "encountered an error!";
					}).
					error(function(data, status, headers, config){
						$scope.oup = "encontered an error!";
					});
				//$scope.oup = "msg has been sent";
				$scope.coms.push({inp:$scope.inp, oup:$scope.oup});
				$scope.inp = "";
			}
		});
