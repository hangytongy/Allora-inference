module.exports.handler = async (event) => {
    return {
      statusCode: 200,
      body: JSON.stringify(
        {
          message: "Group1 Serverless test",
        },
        null,
        2
      ),
    };
  };