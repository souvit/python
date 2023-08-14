const { spawnSync } = require('child_process');

exports.handler = async (event, context) => {
  const pythonProcess = spawnSync('python', ['main.py']);
  const response = {
    statusCode: 200,
    body: JSON.stringify({
      result: pythonProcess.stdout.toString()
    })
  };
  return response;
};

