module.exports = function(grunt) {
    var glob = {
        scss: [
            'static/scss/*.scss'
        ],
        css: [
            'static/css/*.css',
            '!static/css/base.css'
        ]
    };

    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),

        compass: {
            dist: {
                options: {
                    config: 'config/compass.rb'
                }
            }
        },

        watch: {
            css: {
                files: glob.scss,
                tasks: ['compass'],
                options: {
                    livereload: 35729
                }
            },
        }
    });

    grunt.registerTask('default', [
        'watch'
    ])

    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-compass');
}