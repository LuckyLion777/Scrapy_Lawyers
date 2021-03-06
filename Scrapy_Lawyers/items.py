import scrapy


class LawyersItem(scrapy.Item):
    FirstName = scrapy.Field()
    MiddleName = scrapy.Field()
    LastName = scrapy.Field()
    PhoneNumber = scrapy.Field()
    Fax = scrapy.Field()
    Website = scrapy.Field()
    Address = scrapy.Field()
    Description = scrapy.Field()
    Avatar = scrapy.Field()
    # StarRating = scrapy.Field()
    url = scrapy.Field()
    Law_Firm_Logo = scrapy.Field()
    Client_Rating = scrapy.Field()
    Client_Reviews_Number = scrapy.Field()
    Percentage_Recommended = scrapy.Field()
    Peer_Rating = scrapy.Field()
    BirthDate = scrapy.Field()
    Certifications = scrapy.Field()
    Languages = scrapy.Field()
    FirmSize = scrapy.Field()
    Position = scrapy.Field()
    Admission_Details = scrapy.Field()
    Law_School_Attented = scrapy.Field()
    Association_Name = scrapy.Field()
