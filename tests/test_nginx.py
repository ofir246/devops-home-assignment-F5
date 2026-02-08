import os
import sys
import time
import requests
import urllib3
import concurrent.futures

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

NGINX_HOST = os.getenv("NGINX_HOST", "nginx")

# 8080 -> OK HTML page (200)
# 8081 -> Error endpoint (500)
# 8443 -> HTTPS OK page (200) with self-signed cert
HTTP_OK_URL = f"http://{NGINX_HOST}:8080/"
HTTP_ERR_URL = f"http://{NGINX_HOST}:8081/"
HTTPS_OK_URL = f"https://{NGINX_HOST}:8443/"


def fail(msg: str) -> None:
     # Print a clear failure message and exit with code 1.
    # A non-zero exit code tells CI that the test run failed.
    print(f"[FAIL] {msg}", flush=True)
    sys.exit(1)


def assert_true(cond: bool, msg: str) -> None:
    if not cond:
        fail(msg)


def test_http_ok():
    # Check that the "OK" endpoint responds with HTTP 200 and expected HTML content.
    r = requests.get(HTTP_OK_URL, timeout=5)
    assert_true(r.status_code == 200, f"8080 expected 200, got {r.status_code}")
    assert_true("DevOps Assignment - OK" in r.text, "8080 HTML content mismatch")
    print("[PASS] HTTP OK (8080)", flush=True)


def test_http_error():
    # Check that the error endpoint responds with HTTP 500.
    r = requests.get(HTTP_ERR_URL, timeout=5)
    assert_true(r.status_code == 500, f"8081 expected 500, got {r.status_code}")
    print("[PASS] HTTP error server (8081)", flush=True)


def test_https_ok_self_signed():
    # Check that HTTPS works and returns HTTP 200.
    r = requests.get(HTTPS_OK_URL, timeout=5, verify=False)
    assert_true(r.status_code == 200, f"8443 expected 200, got {r.status_code}")
    assert_true("DevOps Assignment - OK" in r.text, "8443 HTML content mismatch")
    print("[PASS] HTTPS OK (8443)", flush=True)


def test_rate_limit():
    # Verify that we are hitting the rate-limited location
    r = requests.get(HTTP_OK_URL, timeout=5)
    assert_true(
        r.headers.get("X-RateLimit-Debug") == "enabled",
        "Rate limit is not enabled on this endpoint"
    )

    print("[PASS] Rate limit configuration is active (verified via header)", flush=True)



def main():
    print("[INFO] Starting tests...", flush=True)

    # Give Nginx a moment to be ready
    time.sleep(1)

    # Run all checks. If any check fails, the script exits with code 1.
    test_http_ok()
    test_http_error()
    test_https_ok_self_signed()
    test_rate_limit()

    # If we reached here, everything passed.
    print("[INFO] All tests passed.", flush=True)
    sys.exit(0)


if __name__ == "__main__":
    main()