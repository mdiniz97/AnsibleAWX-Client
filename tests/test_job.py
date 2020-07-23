
def test_job_summary(api):
    assert api.get_job_summary(150)['id'] == 150

def test_cancel_job(api):
    assert api.cancel_job(150) == False

