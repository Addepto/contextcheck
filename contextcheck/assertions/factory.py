from contextcheck.assertions.assertions import (
    AssertionBase,
    AssertionEval,
    LLMAssertion,
)

assertions_map = {
    "eval": AssertionEval,
    "llm_metric": LLMAssertion,
}


def factory(assert_definition: dict) -> AssertionBase:
    # Take first key from assertions_map present in assert_deffinition
    try:
        kind = next(
            assert_key
            for assert_key in assert_definition.keys()
            if assert_key in assertions_map
        )
    except StopIteration:
        raise ValueError(f"No assertion for definition {assert_definition}")

    assertion_class = assertions_map[kind]
    return assertion_class.model_validate(assert_definition)
