from google.cloud import ndb


class Team(ndb.Model):
    """
    Teams represent FIRST Robotics Competition teams.
    key_name is like 'frc177'
    """

    team_number = ndb.IntegerProperty(required=True)
    name = ndb.TextProperty(indexed=False)
    nickname = ndb.TextProperty(indexed=False)
    school_name = ndb.TextProperty(indexed=False)
    home_cmp = ndb.StringProperty()

    # city, state_prov, country, and postalcode are from FIRST
    city = ndb.StringProperty()  # Equivalent to locality. From FRCAPI
    state_prov = ndb.StringProperty()  # Equivalent to region. From FRCAPI
    country = ndb.StringProperty()  # From FRCAPI
    postalcode = (
        ndb.StringProperty()
    )  # From ElasticSearch only. String because it can be like "95126-1215"

    website = ndb.TextProperty(indexed=False)
    first_tpid = (
        ndb.IntegerProperty()
    )  # from USFIRST. FIRST team ID number. -greg 5/20/2010
    first_tpid_year = (
        ndb.IntegerProperty()
    )  # from USFIRST. Year tpid is applicable for. -greg 9 Jan 2011
    rookie_year = ndb.IntegerProperty()
    motto = ndb.TextProperty(indexed=False)

    created = ndb.DateTimeProperty(auto_now_add=True, indexed=False)
    updated = ndb.DateTimeProperty(auto_now=True, indexed=False)
