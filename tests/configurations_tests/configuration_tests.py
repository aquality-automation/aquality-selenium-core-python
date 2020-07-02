from datetime import timedelta

from hamcrest import assert_that
from hamcrest import equal_to

from aquality_selenium_core.configurations.abc_retry_configuration import (
    AbcRetryConfiguration,
)
from aquality_selenium_core.configurations.duration import Duration
from aquality_selenium_core.configurations.element_cache_configuration import (
    ElementCacheConfiguration,
)
from aquality_selenium_core.configurations.logger_configuration import (
    LoggerConfiguration,
)
from aquality_selenium_core.configurations.retry_configuration import RetryConfiguration
from aquality_selenium_core.configurations.timeout_configuration import (
    TimeoutConfiguration,
)


class TestConfigurations:
    def test_should_be_possible_check_is_enable_element_cache(self, get_profile):
        is_enable = ElementCacheConfiguration(get_profile).enabled
        assert_that(not is_enable, "Element cache is disabled by default")

    def test_should_be_possible_to_get_language(self, get_profile):
        language = LoggerConfiguration(get_profile).language
        assert_that(
            language,
            equal_to("en"),
            "Current language should be got from logger configuration",
        )

    def test_should_be_possible_to_get_retry_configuration(self, get_profile):
        retry_configuration: AbcRetryConfiguration = RetryConfiguration(get_profile)
        assert_that(
            retry_configuration.number,
            equal_to(2),
            "Number of retry attempts timeout should be got",
        )
        a = retry_configuration.polling_interval.milliseconds
        assert_that(
            retry_configuration.polling_interval,
            equal_to(300),
            "Polling interval of retrier should be got",
        )  # todo

    def test_should_be_possible_to_get_timeout_configuration(self, get_profile):

        timeout_configuration = TimeoutConfiguration(get_profile)
        assert_that(
            timeout_configuration.command, equal_to(60), "Command timeout should be got"
        )
        assert_that(
            timeout_configuration.condition,
            equal_to(30),
            "Condition timeout should be got",
        )
        assert_that(
            timeout_configuration.implicit,
            equal_to(0),
            "Implicit timeout should be got",
        )
        assert_that(
            timeout_configuration.polling_interval,
            equal_to(300),
            "Polling interval should be got",
        )
