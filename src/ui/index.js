import './bootstrap'

import UiButton from './UiButton.vue'
import UiCheckbox from './UiCheckbox.vue'
import UiModal from './UiModal.vue'
import UiProgressCircular from './UiProgressCircular.vue'
import UiProgressLinear from './UiProgressLinear.vue'
import UiTextbox from './UiTextbox.vue'

const Keen = {
  UiButton,
  UiCheckbox,
  UiModal,
  UiProgressCircular,
  UiProgressLinear,
  UiTextbox,
  install (Vue) {
    Vue.component('ui-button', UiButton)
    Vue.component('ui-checkbox', UiCheckbox)
    Vue.component('ui-modal', UiModal)
    Vue.component('ui-progress-circular', UiProgressCircular)
    Vue.component('ui-progress-linear', UiProgressLinear)
    Vue.component('ui-textbox', UiTextbox)
  }
}

// Automatically install Keen UI if Vue is available globally
if (typeof window !== 'undefined' && window.Vue) {
  window.Vue.use(Keen)
}

export default Keen

export { UiButton }
export { UiCheckbox }
export { UiModal }
export { UiProgressCircular }
export { UiProgressLinear }
export { UiTextbox }
