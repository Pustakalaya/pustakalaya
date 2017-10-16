'use strict';

var gulp = require('gulp');
var sass = require('gulp-sass');
let cleanCSS = require('gulp-clean-css');

gulp.task('sass', function () {
  return gulp.src('./static/base_assets/base.scss')
    .pipe(sass().on('error', sass.logError))
    .pipe(cleanCSS({compatibility: 'ie8'}))
    .pipe(gulp.dest('./static/base_assets/css/'));
});

gulp.task('sass:watch', function () {
  gulp.watch('./static/base_assets/base.scss', ['sass']);
});