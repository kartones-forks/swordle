import CopyWebpackPlugin from "copy-webpack-plugin";
import path from "path";

// Disabling source maps
export default (config, env, _helpers) => {
  if (env.isProd) {
    config.devtool = false;
  }

  config.plugins.push(
    new CopyWebpackPlugin({
      patterns: [
        {
          from: "*",
          context: path.resolve(__dirname, "src/assets"),
        },
      ],
    })
  );
};
