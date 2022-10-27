class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        for email in emails:
            local, domain = email.split('@')
            local = local.replace('.','')
            if '+' in local:
                local = local.split('+')[0]
                
            email = local+"@"+domain
            unique_emails.add(email)
        return len(unique_emails)