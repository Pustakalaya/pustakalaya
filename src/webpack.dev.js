const merge = require('webpack-merge');
const common = require('./webpack.common.js');
const BundleTracker = require('webpack-bundle-tracker')

common.devtool = "#eval-source-map"
common.plugins = common.plugins.concat([
  new BundleTracker({filename: './webpack-stats-local.json'}),
])


  module.exports = merge(common, {
    devServer: {
      contentBase: './dist'
    }
  });