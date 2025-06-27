document.addEventListener("DOMContentLoaded", function () {
  const check = document.getElementById("anonimo");
  const dados = document.getElementById("identificacao");
  const inputs = dados.querySelectorAll("input");

  const cepInput = document.querySelector('input[name="cep"]');
  cepInput.addEventListener("blur", buscarEnderecoPorCep);

  check.addEventListener("change", function () {
    if (check.checked) {
      dados.style.display = "none";
      inputs.forEach((input) => (input.required = false));
    } else {
      dados.style.display = "block";
      inputs.forEach((input) => (input.required = true));
    }
  });

  function buscarEnderecoPorCep() {
    const cep = document
      .querySelector('input[name="cep"]')
      .value.replace(/\D/g, "");

    if (cep.length !== 8) {
      return;
    }

    fetch(`https://viacep.com.br/ws/${cep}/json/`)
      .then((response) => response.json())
      .then((data) => {
        if (!data.erro) {
          document.querySelector('input[name="logradouro"]').value =
            data.logradouro || "";
          document.querySelector('input[name="bairro"]').value =
            data.bairro || "";
          document.querySelector('input[name="cidade"]').value =
            data.localidade || "";
          document.querySelector('select[name="uf"]').value = data.uf || "";
        }
      });
  }
});
