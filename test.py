from src import *


def test_create_get_change_user():
    # ----Create user------
    exec_data = ExecuteData(username=rand_string_generator(5), password=rand_string_generator(5),
                            email=rand_email_generator(5))
    post_request = test_requester.create_user(data=exec_data.PostData(), headers=exec_data.Header())
    assert post_request.status_code == requests.codes.created, Message(str(post_request.content),
                                                                       exec_data.username, exec_data.password,
                                                                       exec_data.email)
    assert post_request.json()['data']['attributes']['username'] == exec_data.username

    # ----Get user after post------
    get_request_after_post = test_requester.get_user(exec_data.username)
    assert get_request_after_post.status_code == requests.codes.ok, Message(str(get_request_after_post.content),
                                                                            exec_data.username, exec_data.password,
                                                                            exec_data.email)
    assert get_request_after_post.json()['data']['attributes']['username'] == exec_data.username
    exec_data.user_id = get_request_after_post.json()['data']['id']

    # -----Change user------
    exec_data.username = rand_string_generator(5)
    patch_request = test_requester.change_user(user_id=exec_data.user_id, data=exec_data.PatchData(),
                                               headers=exec_data.Header())
    assert patch_request.status_code == requests.codes.no_content, Message(str(patch_request.content),
                                                                           exec_data.username, exec_data.password,
                                                                           exec_data.email)

    # ----Get user after patch------
    get_request_after_patch = test_requester.get_user(exec_data.username)
    assert get_request_after_patch.status_code == requests.codes.ok, Message(str(get_request_after_patch.content),
                                                                             exec_data.username,
                                                                             exec_data.password, exec_data.email)
    assert get_request_after_patch.json()['data']['attributes']['username'] == exec_data.username
    assert exec_data.user_id == get_request_after_patch.json()['data']['id']


def test_create_user_with_same_data():
    # ----Create user------
    exec_data = ExecuteData(username=rand_string_generator(5), password=rand_string_generator(5),
                            email=rand_email_generator(5))
    post_request = test_requester.create_user(data=exec_data.PostData(), headers=exec_data.Header())
    assert post_request.status_code == requests.codes.created, Message(str(post_request.content),
                                                                       exec_data.username, exec_data.password,
                                                                       exec_data.email)
    assert post_request.json()['data']['attributes']['username'] == exec_data.username

    # ----Create user with same username------
    exec_data_1 = ExecuteData(username=exec_data.username, password=rand_string_generator(5),
                              email=rand_email_generator(5))
    post_request = test_requester.create_user(data=exec_data_1.PostData(), headers=exec_data_1.Header())
    assert post_request.status_code == requests.codes.conflict, Message(str(post_request.content),
                                                                        exec_data_1.username, exec_data_1.password,
                                                                        exec_data_1.email)

    # ----Create user with same email------
    exec_data_2 = ExecuteData(username=rand_string_generator(5), password=rand_string_generator(5),
                              email=exec_data.email)
    post_request = test_requester.create_user(data=exec_data_2.PostData(), headers=exec_data_2.Header())
    assert post_request.status_code == requests.codes.conflict, Message(str(post_request.content),
                                                                        exec_data_2.username, exec_data_2.password,
                                                                        exec_data_2.email)
    # ----Create user with same email------
    exec_data_3 = ExecuteData(username=exec_data.username, password=rand_string_generator(5),
                              email=exec_data.email)
    post_request = test_requester.create_user(data=exec_data_3.PostData(), headers=exec_data_3.Header())
    assert post_request.status_code == requests.codes.conflict, Message(str(post_request.content),
                                                                        exec_data_3.username, exec_data_3.password,
                                                                        exec_data_3.email)


def test_create_user_with_different_password_length():
    # ----Create user with 32 chars password------
    exec_data = ExecuteData(username=rand_string_generator(5), password=rand_string_generator(32),
                            email=rand_email_generator(5))
    post_request = test_requester.create_user(data=exec_data.PostData(), headers=exec_data.Header())
    assert post_request.status_code == requests.codes.created, Message(str(post_request.content),
                                                                       exec_data.username, exec_data.password,
                                                                       exec_data.email)
    assert post_request.json()['data']['attributes']['username'] == exec_data.username

    # ----Create user with 65 chars password------
    exec_data_1 = ExecuteData(username=rand_string_generator(5), password=rand_string_generator(65),
                              email=rand_email_generator(5))
    post_request = test_requester.create_user(data=exec_data_1.PostData(), headers=exec_data_1.Header())
    assert post_request.status_code == requests.codes.unprocessable_entity, Message(str(post_request.content),
                                                                                    exec_data_1.username,
                                                                                    exec_data_1.password,
                                                                                    exec_data_1.email)

    # ----Create user with 3 chars password------
    exec_data_2 = ExecuteData(username=rand_string_generator(5), password=rand_string_generator(3),
                              email=rand_email_generator(5))
    post_request = test_requester.create_user(data=exec_data_2.PostData(), headers=exec_data_2.Header())
    assert post_request.status_code == requests.codes.unprocessable_entity, Message(str(exec_data_2.content),
                                                                                    exec_data_2.username,
                                                                                    exec_data_2.password,
                                                                                    exec_data_2.email)


def test_create_user_with_wrong_content_type():
    # ----Create user with wrong content-type------
    exec_data = ExecuteData(username=rand_string_generator(5), password=rand_string_generator(32),
                            email=rand_email_generator(5), content_type_var=rand_string_generator(5))
    post_request = test_requester.create_user(data=exec_data.PostData(), headers=exec_data.Header())
    assert post_request.status_code == requests.codes.unsupported_media_type, Message(str(post_request.content),
                                                                                      exec_data.username,
                                                                                      exec_data.password,
                                                                                      exec_data.email)
