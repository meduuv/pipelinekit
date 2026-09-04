import unittest
from pipelinekit import summarize

class PipelineKitTests(unittest.TestCase):
    def test_summary(self):
        self.assertEqual(summarize([{"status":"ok"},{"status":"failed"},{"status":"ok"}]), {"failed":1,"ok":2})

if __name__ == "__main__":
    unittest.main()
