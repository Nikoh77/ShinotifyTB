import logging
import requests
import json  # for debug only, can be removed when all work fine...
import http.client

logger = logging.getLogger(name=__name__)

async def queryUrl(
    url, method="get", data=None, debug=False
) -> None | requests.Response:
    methods = ["get", "post", "put", "delete"]
    if method in methods:
        http_method = getattr(requests, method)
        response: requests.Response
        try:
            if method == ("get" or "delete"):
                response = http_method(url=url, data=data)
            else:
                response = http_method(url=url, data=data)
            if response.status_code != 200:
                logger.info(
                    msg=f"Error {response.status_code} something went wrong, request error."
                )
            else:
                logger.debug(msg="OK, request done.")
                if debug:
                    logger.info(
                        msg=f"\nRequest method: {method}\nType of data: "
                        f"{type(data)}\nData: {json.dumps(obj=data, indent=4)}\nServer response:\n{response.text}"
                    )
                return response
        except requests.exceptions.RequestException as e:
            logger.critical(
                msg=f"Error something went wrong, request-->connection error: \n{e}"
            )
    else:
        logger.error(msg=f"Invalid method: {method}")
    return None


if __name__ == "__main__":
    raise SystemExit
