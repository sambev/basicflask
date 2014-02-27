module.exports = function(grunt) {
    var glob = {
        scss: [
            'static/scss/*.scss'
        ]
    };

    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),

        sass: {
            dist: {
                options: {
                    quiet: true,
                    style: 'compressed'
                },
                files: {
                    'static/css/base.css': 'static/scss/base.scss',
                }
            }
        },

        scsslint: {
            allFiles: ['static/scss/*.scss'],
            options: {
                config: 'config/scss-lint.yml',
                reporterOutput: 'build/lint/scss-lint-report.xml'
            },
        },

        watch: {
            scss: {
                files: glob.scss,
                tasks: ['sass', 'quality']
            },
        }
    });

    grunt.registerTask('default', ['watch']);
    grunt.registerTask('scss', ['scss']);
    grunt.registerTask('quality', ['scsslint']);

    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-sass');
    grunt.loadNpmTasks('grunt-scss-lint');
}