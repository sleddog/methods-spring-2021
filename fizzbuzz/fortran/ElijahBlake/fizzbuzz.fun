test_suite fizzbuzz

setup
  ! Place code here that should run before each test
  c = 3
end setup

teardown
  ! This code runs immediately after each test
end teardown

test radius_is_stored_properly
    assert_real_equal(radius, 1.5d0)
end test

end test_suite