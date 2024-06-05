# Postmortem Report: WordPress Server Outage

Issue Summary

    Duration: The outage lasted for approximately 20 minutes, starting at 07:11 AM GMT and ending at 07:32 AM GMT on March 24, 2017.
    Impact: The WordPress website was completely inaccessible to users, returning a 500 Internal Server Error. Approximately 100% of the users were affected during this period.
    Root Cause: The root cause was missing files in the /var/www/html directory, which are essential for the WordPress application to function correctly.

Timeline

    07:11 AM GMT: The issue was detected through a monitoring alert indicating the website was returning a 500 Internal Server Error.
    07:12 AM GMT: Initial investigation began by checking the server status using curl -sI 127.0.0.1.
    07:13 AM GMT: The 500 Internal Server Error was confirmed. Assumptions were made that the issue could be related to the Apache or PHP configuration.
    07:15 AM GMT: Further investigation involved checking the Apache error logs and the PHP configuration.
    07:18 AM GMT: It was identified that the /var/www/html directory had missing files, causing the server to fail in loading the necessary WordPress files.
    07:20 AM GMT: The issue was escalated to the DevOps team.
    07:23 AM GMT: The DevOps team decided to use Puppet to restore the missing files.
    07:25 AM GMT: The Puppet script 0-strace_is_your_friend.pp was applied to fix the missing files issue.
    07:30 AM GMT: The Puppet script executed successfully, restoring the missing files.
    07:32 AM GMT: The server was verified to be functioning correctly with a successful curl -sI 127.0.0.1:80 returning HTTP 200 OK.

Root Cause and Resolution

    Root Cause: The missing files in the /var/www/html directory caused the WordPress application to fail, resulting in a 500 Internal Server Error. These files were likely deleted or moved due to a misconfiguration or an unintended script execution.
    Resolution: The issue was resolved by applying a Puppet script (0-strace_is_your_friend.pp) that restored the missing files in the /var/www/html directory. This script was executed successfully, and the server returned to normal operation.

Corrective and Preventative Measures

    Improvements and Fixes:
        Implement stricter controls and audits on file changes within the /var/www/html directory.
        Enhance monitoring to detect and alert on critical file changes or deletions in real-time.
        Conduct regular backups of the /var/www/html directory to facilitate quick restoration in case of future issues.
    Tasks:

 Patch Nginx server to ensure it handles similar issues more gracefully.
 Add monitoring for file integrity in the /var/www/html directory.
 Review and tighten access permissions to the /var/www/html directory to prevent unauthorized changes.
 Schedule regular audits of server configurations and scripts that interact with the /var/www/html directory.
 Conduct training for the team on the importance of maintaining the integrity of critical application directories.
