There is an Apache-style access log at `/app/access.log`.

Parse the log and write a JSON summary report to `/app/report.json` with
exactly these three keys:

- `total_requests` (int): the total number of log lines in the file.
- `unique_ips` (int): the number of distinct client IP addresses that
  appear in the log.
- `top_path` (string): the request path (e.g. `/index.html`) that appears
  in the most requests. If there is a tie, any one of the tied paths is
  acceptable.

The output must be valid JSON containing only these three keys.
