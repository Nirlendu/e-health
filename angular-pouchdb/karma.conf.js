/*
 *
 * Copyright - Nirlendu Saha
 * author - nirlendu@gmail.com
 *
 */

// Karma - Jasmine configuration file

module.exports = function(config) {
config.set({
    frameworks: ['jasmine'],
    files: [
        'assets/js/angular/angular.min.js',
        'assets/js/angular/angular-mocks.js',
        'assets/js/pouchdb.min.js',
        'assets/js/angular-pouchdb.min.js',
        'assets/js/angular_app.js',
        'test/*.js'
    ],
    browsers: [
        'Chrome',
    ],
    autoWatch: false,
    singleRun: true,
    reporters: [
        'progress',
        'coverage'
    ],
    preprocessors: {
        'angular-pouchdb.js': ['coverage']
    },
        coverageReporter: {
        dir: 'test/coverage',
        reporters: [{
                type: 'lcov',
                subdir: 'lcov'
            }]
        }
    });
};