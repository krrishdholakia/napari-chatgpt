from src.napari_chatgpt.tools.functions_info import PythonFunctionsInfoTool


def test_tools():
    tool = PythonFunctionsInfoTool()

    query = "skimage.morphology.watershed"
    result = tool._run(query)
    assert len(result) < 300
    assert 'markers = None' in result

    query = "*skimage.morphology.watershed"
    result = tool._run(query)
    assert len(result) > 300
    assert 'markers' in result
