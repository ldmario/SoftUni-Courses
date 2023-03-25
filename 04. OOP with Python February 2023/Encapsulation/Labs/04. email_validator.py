class EmailValidator:
    def __init__(self, min_length: int, mails: list, domains: list):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name):
        return len(name) >= self.min_length

    def __is_mail_valid(self, mail):
        return mail in self.mails

    def __is_domain_valid(self, domain):
        return domain in self.domains

    def validate(self, email):
        return all([self.__is_name_valid(email.split("@")[0]),
                    self.__is_mail_valid(email.split("@")[1].split(".")[0]),
                    self.__is_domain_valid(email.split(".")[1])])
