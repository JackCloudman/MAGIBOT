class CoreMessage():
    src = None
    dest = None
    text = None
    img = None
    audio = None
    def __init__(self,m_type=None):
        self.m_type = m_type
