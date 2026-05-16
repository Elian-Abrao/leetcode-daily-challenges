class Solution:
    def maskPII(self, s: str) -> str:
        # Distinguish between email and phone by checking for '@' symbol
        if '@' in s:
            return self._mask_email(s)
        else:
            return self._mask_phone(s)
    
    def _mask_email(self, email: str) -> str:
        # Convert entire email to lowercase first
        email = email.lower()
        
        # Split by '@' to separate name and domain
        name, domain = email.split('@')
        
        # Mask the name: first char + "*****" + last char
        # Always use exactly 5 asterisks regardless of original name length
        masked_name = name[0] + '*****' + name[-1]
        
        # Reconstruct the masked email
        return masked_name + '@' + domain
    
    def _mask_phone(self, phone: str) -> str:
        # Extract only digits from the phone number
        digits = ''.join(c for c in phone if c.isdigit())
        
        # Last 10 digits are the local number, rest is country code
        local = digits[-10:]
        country_code_length = len(digits) - 10
        
        # Last 4 digits of local number are shown
        last_four = local[-4:]
        
        # Build the masked phone number based on country code length
        if country_code_length == 0:
            # No country code: "***-***-XXXX"
            return f"***-***-{last_four}"
        elif country_code_length == 1:
            # 1-digit country code: "+*-***-***-XXXX"
            return f"+*-***-***-{last_four}"
        elif country_code_length == 2:
            # 2-digit country code: "+**-***-***-XXXX"
            return f"+**-***-***-{last_four}"
        else:  # country_code_length == 3
            # 3-digit country code: "+***-***-***-XXXX"
            return f"+***-***-***-{last_four}"