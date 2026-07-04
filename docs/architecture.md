                           User
                             │
                             ▼
                    URL Validator
                             │
          ┌──────────────────┴──────────────────┐
          │                                     │
          ▼                                     ▼
    DNS Resolver                       Header Collector
          │                                     │
          ▼                                     ▼
    Port Scanner                        SSL Analyzer
          │                                     │
          ▼                                     ▼
     Service Detector               Security Header Analyzer
          │                                     │
          └──────────────────┬──────────────────┘
                             ▼
                  Vulnerability Engine
                             │
                             ▼
                       Risk Engine
                             │
                             ▼
                     Report Generator
                     