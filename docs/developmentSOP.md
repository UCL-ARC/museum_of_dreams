# Standard development procedure

This document outlines the recommended way we develop and publish features for this project.

#### 1. Begin to develop code locally on new branch

#### 2. If you are working on a feature that needs to be tested on staging whilst in development, use the `dev-feature-test-pipeline` pipeline and edit it to point towards your branch. You will have to manually release the change. Be sure to notify your colleagues _before_ doing this to ensure there is no conflict in the versions.

#### 3. Once you've finished developing the feature, open a PR to `development`. Once merged, double check the behaviour is as expected on staging.

#### 4. Once confirmed, open a PR to `main` and once merged, check the behaviour is as expected on production. You may wish to inform the researchers via email.

#### 5. On the the next! 😁

If you have any questions, contact [Amanda Ho-Lyn](mailto:a.ho-lyn@ucl.ac.uk)
